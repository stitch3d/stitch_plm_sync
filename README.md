# STITCH PLM Sync
Documentation and example code for importing your PLM data into STITCH systems

# API
STITCH provides an API to upload PLM data to STITCH systems.
Currently, we only support uploading CSV and XLS files. In the future, support for JSON upload will be added as well.

The API is hosted at the address https://plm-store-api.stitch.fashion/, and currently only has one endpoint: https://plm-store-api.stitch.fashion/plm/import/
You can use it to upload one and only one file as a form per request. The file can be either a .xlsx file, or a .csv file. If you use the CSV format, please use ';' as the delimiter.
You need to include the following headers for the request:  
```
x-api-key: <your stitch api key>  
x-stitch-client: plm_uploader
```

Both the CSV and XLS need to comply with the following specs:
- The file must have a header
- The following columns are mandatory:
    -  `Style Name` 
    -  `Style Code`
    -  `Option Name` 
    -  `Option Code` 
    -  `Season` 

Style code and option code should be unique IDs by which an entry can be identified. The uniqueness is checked on per-season basis 
(so that repeating style+option codes are still allowed if they are in different seasons. This can be used for, for example, carry-over styles).
- All the rest of the fields will be made available in STITCH systems for lookup based on provided combination of Season + Style/Option Codes/Names 