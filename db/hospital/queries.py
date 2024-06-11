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

sel_deps_wards = (
    '  select d.name as department,'
    '         w.name as ward       '
    '    from departments as d     '
    '    join wards as w           '
    '      on d.id = dep_id        '
    'order by d.id, w.id;          '
)
sel_doctors_specs = '''
  select concat_ws(' ', last_name, first_name, patr_name) as full_name,
         s.name as spec
    from doctors as d
    join doctors_specs as ds
      on d.id = doctor_id
    join specializations as s
      on spec_id = s.id
order by full_name;
'''

