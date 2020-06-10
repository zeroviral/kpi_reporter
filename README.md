# KPI Reporter
A grassroots reporter to sift information and curate reminders based on multiple sources of data.

To run the server locally, please have Docker Engine installed and running.

You should be within the following folder:

```log
<path_to_your_project>/kpi_reporter
```

To then run the following command:
```shell script
docker-compose up --build
```

After this, the server (with default settings) should then be running on 
```html
http://localhost:5000/
```

## Usage

All responses will have the form:

```json
{
  "reminder": "<title_of_reminder>",
  "complete": "<boolean>",
  "identifier": "<unique_id>", 
  "created_at": "<datetime.datetime> timestamp at point of db entry."
}
```

## List Of all reminders sorted by object reference

`GET /reminders`

**Response**

- `200 OK` on success

```json
[
    {
      "reminder": "This is a reminder!",
      "completed": "True",
      "identifier": "<some_unique_ID>",
      "created_at": "[ 06-09-2020 21:21:48 PM ]"
    },
    {
      "reminder": "This is ANOTHER reminder!",
      "completed": "False",
      "identifier": "<some_other_unique_ID>",
      "created_at": "[ 06-09-2020 23:21:48 PM ]"
    }
]
```

### Adding/Creating a Reminder

**Definition**

`POST /create_reminder`

**Arguments**

- `"reminder":string` A reminder taken from an input.
- `"completed":boolean` A boolean value based on completion of reminder/task.

If a reminder with an identifier already exists, it will simply be overwritten.

**Response**

- `201 Created` on success:
```json
{
  "reminder": "This is a reminder!",
  "completed": "True",
  "identifier": "<some_ID>",
  "created_at": "[ 06-09-2020 21:21:48 PM ]"
}
```
- `404 NOT FOUND` if the reminder does not exist

## Delete a Reminder

**Response**

**Definition**

`DELETE /reminders/<identifier>`

- `404 NOT FOUND` if the reminder does not exist.

- `204 DELETED` if the reminder exists, and is deleted.