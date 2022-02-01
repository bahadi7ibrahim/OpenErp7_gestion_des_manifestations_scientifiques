{
    'name':"Gestion Des Manifestation Scientifiques à l'ENSAH",
    'version':'1.0',
    'author':'CHACHI Ayoub & BAHADI Ibrahim',
    'category':'Manifestations management',
    'icon': "Gestion des manifestations scientifiques/static/icon.png",
    'sequence':1,
    'description': """
        Module de la gestion des manifestations scientifiques
        *Gestion des évenements
        *Gestion des participants
        *Gestion des partenaires
    

    """,
    'website':'',
    'images':[],
    'depends':['base'],
    'data':['gms_ensah_participant_view.xml','gms_ensah_sponsor_view.xml', 'gms_ensah_manifestation_view.xml', 'gms_ensah_organisateur_view.xml', 'gms_ensah_local_view.xml', 'gms_ensah_intervenant_view.xml', 
    'gms_ensah_responsable_view.xml','workflow/workflow_manifestation.xml'],
    'init_xml' : [],
    'update_xml' : [],
    'js':[],
    'qweb':[],
    'css':[],
    'demo':[],
    'test':[],
    "installable": True,
    "auto_install": False
}