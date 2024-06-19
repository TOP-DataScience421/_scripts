ins_departments = (
    'insert into departments'
    '  (name)'
    'values'
    '  (%s)'
)
ins_sponsors = (
    'insert into sponsors'
    '  (name)'
    'values'
    '  (%s)'
)
ins_specializations = (
    'insert into specializations'
    '  (name)'
    'values'
    '  (%s)'
)
ins_wards = (
    'insert into wards'
    '  (dep_id, name)'
    'values'
    '  (%s, %s)'
)
ins_donations = (
    'insert into donations'
    '  (sponsor_id, dep_id, date, amount)'
    'values'
    '  (%s, %s, %s, %s)'
)
ins_doctors = (
    'insert into doctors'
    '  (dep_id, last_name, first_name, patr_name, salary, premium)'
    'values'
    '  (%s, %s, %s, %s, %s, %s)'
)
ins_doctors_specs = (
    'insert into doctors_specs'
    '  (doctor_id, spec_id)'
    'values'
    '  (%s, %s)'
)
ins_vacations = (
    'insert into vacations'
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

sel_deps_wards_count = '''
  select d.name,
         count(*)
    from departments as d
    join wards as w
      on d.id = dep_id
group by d.name;
'''
sel_vacation_days_by_weeks = '''
select 
  case when end_date-start_date <= 7 then 'до 1 недели'
       when end_date-start_date <= 14 then 'от 1 до 2 недель'
       else 'больше 2 недель'
  end as "days",
  count(*) as "count"
from 
  vacations
group by
  "days";
'''

sel_doctors_specs_full = '''
   select last_name || ' ' || first_name || ' ' || patr_name as full_name,
          s.name as spec
     from doctors as d
full join doctors_specs 
       on d.id = doctor_id
full join specializations as s 
       on spec_id = s.id 
 order by full_name;
'''
sel_full_specs_cnt = '''
   select case when s.name is not null then s.name
               else 'Младший мед.персонал'
          end as spec,
          count(d.id) as "total people"
     from doctors as d
full join doctors_specs 
       on d.id = doctor_id
full join specializations as s 
       on spec_id = s.id 
 group by "spec"
 order by "total people" desc;
'''
