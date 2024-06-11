ins_departments = (
    'insert departments'
    '  (name)'
    'values'
    '  (%s)'
)
ins_sponsors = (
    'insert sponsors'
    '  (name)'
    'values'
    '  (%s)'
)
ins_specializations = (
    'insert specializations'
    '  (name)'
    'values'
    '  (%s)'
)
ins_wards = (
    'insert wards'
    '  (dep_id, name)'
    'values'
    '  (%s, %s)'
)
ins_donations = (
    'insert donations'
    '  (sponsor_id, dep_id, date, amount)'
    'values'
    '  (%s, %s, %s, %s)'
)
ins_doctors = (
    'insert doctors'
    '  (dep_id, last_name, first_name, patr_name, salary, premium)'
    'values'
    '  (%s, %s, %s, %s, %s, %s)'
)
ins_doctors_specs = (
    'insert doctors_specs'
    '  (doctor_id, spec_id)'
    'values'
    '  (%s, %s)'
)
ins_vacations = (
    'insert vacations'
    '  (doctor_id, start_date, end_date)'
    'values'
    '  (%s, %s, %s)'
)

