{
  'name': 'modi hospital ',
  'version': '15',
  'category': 'Hospital',
  'sequence': -1,
  'author': 'Garvit modi',
  'website': "https://www. om_hospital.com",
  'company': 'Tcb infotech Solution',
  'maintainer': 'tcb infotech Solutions',
  'summary': 'Record patient Details',
  "description": """To manage Hospial""",
  'depends': ['mail'],
   'data': [

     'security/ir.model.access.csv',
     "views/menu.xml",
     "views/patient_view.xml",
     "views/femaie_patient.xml",
     "views/appointment_view.xml",



  ],
  'qweb': [],
  "license": "AGPL-3",
  'installable': True,
  'auto_install': False,
}