# kpi_reporter
A grassroots reporter to sift information and curate KPIs based on multiple sources of data.


## Usage

All responses will have the form:

```json
{
  "data": "Some data here bla blah blahhhh",
  "message": "If you sell your turnips on Sunday, you make more bells."
}
```

## List Of all KPIs sorted by object reference

`GET /kpis`

**Response**

- `200 OK` on success

```json
    [
      {
        "identifier": "KPIs Completed Today",
        "name": "KPIs Complete (24HR)",
        "task_bucket": "24HR"
      },

      {
        "identifier": "KPIs Completed For the Week",
        "name": "KPIs Completed (7D)",
        "task_bucket": "7D"
      }
    ]
```

### Adding KPIs

**Definition**

`POST /create_kpis`

**Arguments**

- `"identifier":string` A global identifier for a KPi, unique.
- `"group":string` A name for the KPI group. Can ONLY be Complete/Incomplete.
- `"created_at":string` The timestamp at which point the KPI was created.

If a KPI with an identifier already exists, it will simply be overwritten.

**Response**

- `201 Created` on success:
```json
{
  "identifier": "Your KPI Title",
  "group": "Complete",
  "created_at": "[ 06-09-2020 21:21:48 PM ]"
}
```
- `404 NOT FOUND` if the KPI does not exist

## Delete a KPI

**Response**

**Definition**

`DELETE /kpis/<identifier>`

- `404 NOT FOUND` if the KPI does not exist