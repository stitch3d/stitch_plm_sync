# STITCH PLM Sync
Documentation and example code for importing your PLM data into STITCH systems

# API
STITCH provides an API to upload PLM data to STITCH systems.
Currently, we only support uploading CSV and XLS files. In the future, support for JSON upload will be added as well.


The API is hosted at the address https://plm-store-api.stitch.fashion/.

You need to include the following headers for all requests to all endpoints:  
```
x-api-key: <your stitch api key>  
x-stitch-client: plm_uploader
```


## Start sync endpoint
The endpoint for importing data is:
https://plm-store-api.stitch.fashion/plm/import/

You can use it to upload one and only one file as a form-data body per request. The file can be either a .xls file, or a .csv file. If you use the CSV format, use ';' as the delimiter.

Both the CSV and XLS need to comply with the following specs:
- The file must have a header (first row must contain column names)
- The following columns are mandatory:
    -  `Style Name` 
    -  `Style Code`
    -  `Option Name` 
    -  `Option Code` 
    -  `Season` 

Style code and option code should be unique IDs by which an entry can be identified. The uniqueness is checked on per-season basis 
(so that repeating style+option codes are still allowed if they are in different seasons. This can be used for, for example, carry-over styles).
- All the rest of the fields will be made available in STITCH systems for lookup based on provided combination of Season + Style/Option Codes/Names 

The endpoint will send along a `sync_result_id` in the successful responses body. You can use this ID to check in on progress and get details of the result of the import, as described in the next section.

## Getting result reports
You can use the received `sync_result_id` to query the status of the processing of the information, and, when done, its results, using the following endpoint:
https://plm-store-api.stitch.fashion/plm/import/<sync_result_id>/

The body of response of the endpoint will have the following fields:
- `status`: can be one of the following values:
   - `SUCCESS`: the file has been processed completely. Refer to the other fields for results
   - `FAILURE`: there has been an unexpected error while processing the file. Check that the file complies with specifications, if the error persists, contact STITCH.
   - `PENDING`: the processing of the file is in progress
- `created`: amount of records created
- `updated`: amount of records updated
- `failed`: amount of records skipped (for example, due to missing required fields)

