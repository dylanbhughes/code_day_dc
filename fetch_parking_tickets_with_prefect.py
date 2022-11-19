import pandas as pd
import pendulum
import requests
from prefect import flow, task


@task(retries=5, retry_delay_seconds=3600)
def fetch_tickets_by_day(day: pendulum.datetime) -> list:
    where = f"""ADDDATE >= DATE '{day.format("YYYY-MM-DD HH:mm:ss")}' - INTERVAL '24' HOUR"""

    response = requests.get(
        url=f"https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_APPS/SR_30days_Open/MapServer/8/query?where={where}&outFields=*&outSR=4326&f=json",
    )

    if not response.ok:
        raise ValueError(f"Response should be ok, {response}")

    response_json = response.json()
    records = response_json["features"]
    tickets = []

    for record in records:
        tickets.append(record["attributes"])

    return tickets


@task
def convert_ticket_dates(tickets_list: list) -> pd.DataFrame:
    tickets_df = pd.DataFrame(tickets_list)

    columns = ["ADDDATE", "RESOLUTIONDATE", "SERVICEDUEDATE", "SERVICEORDERDATE"]
    for column in columns:
        tickets_df[column] = pd.to_datetime(tickets_df[column], unit="ms")

    return tickets_df


@task
def write_tickets_to_csv(tickets_df: pd.DataFrame) -> None:
    tickets_df.to_csv(f"""parking_tickets_{pendulum.now().to_iso8601_string()}.csv""")


@flow(name="Fetch Parking Tickets", retries=5)
def fetch_parking_tickets(
    date=pendulum.today().subtract(days=1),
) -> None:
    tickets = fetch_tickets_by_day(day=pendulum.today().subtract(days=1))
    tickets_df = convert_ticket_dates(tickets)
    write_tickets_to_csv(tickets_df)


if __name__ == "__main__":
    fetch_parking_tickets()
