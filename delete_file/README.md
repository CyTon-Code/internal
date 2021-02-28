# File deletion function.

###### What can you expect from her:

- 'True' - the file existed and was deleted (the address is correct).
- 'False' - The file did not exist and was not deleted (wrong address).
- 'Exception' or 'None' - file exists and has not been deleted.

###### On A Note:

- If you only use the function for the file delete effect, then in this case: both False and True say: The specified
  file is no longer exists at the specified address. And if you check the return type: type
  (delete_file (link)) == bool then True (file deleted) and False (file not deleted).
