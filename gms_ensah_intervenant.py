from osv import osv,fields
# import openerp


class gms_ensah_intervenant(osv.osv):
    _name= 'gms.ensah.intervenant'
    _columns={
        'image':fields.binary('photo_intervenant', filters="*.png"),
        'name':fields.char('Nom Complet',required=True ) ,
        'email':fields.char('Email', required=True)  ,
        'phone':fields.char('Telephone', required=True)  ,
        'nationalite': fields.char('Nationalite') ,
        
        'id_manifestation':fields.many2one('gms.ensah.manifestation','Manifestation', ondelete='cascade'),


   
    }
gms_ensah_intervenant()