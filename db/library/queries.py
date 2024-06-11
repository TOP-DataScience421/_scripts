select_all_authors = 'select * from authors'

select_authors_fullname = (
    'select'
    '  concat_ws(" ", first_name, last_name)'
    'from'
    '  authors'
)
