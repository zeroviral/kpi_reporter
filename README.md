# reminders_reporter
A grassroots reporter to sift information and curate reminders based on multiple sources of data.


## Usage

All responses will have the form:

```json
{
  "title_of_reminders": "<title_of_reminders>",
  "complete": "<boolean>",
  "reminders_details": "<details> if applicable, else <title_of_reminders>",
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
        "identifier": "reminders Completed Today",
        "name": "reminders Complete (24HR)",
        "task_bucket": "24HR"
      },

      {
        "identifier": "reminders Completed For the Week",
        "name": "reminders Completed (7D)",
        "task_bucket": "7D"
      }
    ]
```

### Adding reminders

**Definition**

`POST /create_reminders`

**Arguments**

- `"identifier":string` A global identifier for a reminders, unique.
- `"group":string` A name for the reminders group. Can ONLY be Complete/Incomplete.
- `"created_at":string` The timestamp at which point the reminders was created.

If a reminders with an identifier already exists, it will simply be overwritten.

**Response**

- `201 Created` on success:
```json
{
  "identifier": "Your reminders Title",
  "group": "Complete",
  "created_at": "[ 06-09-2020 21:21:48 PM ]"
}
```
- `404 NOT FOUND` if the reminders does not exist

## Delete a reminders

**Response**

**Definition**

`DELETE /reminders/<identifier>`

- `404 NOT FOUND` if the reminders does not exist