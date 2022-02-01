from osv import osv,fields
# import openerp


class gms_ensah_sponsor(osv.osv):
    _name= 'gms.ensah.sponsor'
    _columns={
        'image': fields.binary('logo_sponsor', filters="*.png"),
        'name':fields.char('Nom', required=True) ,
        'email':fields.char('Email', required=True) ,
        'phone':fields.char('Telephone', required=True) ,
        'type': fields.selection(selection=[('entreprise','Entreprise'),('association','Association'),('individu','Individu')], string='Type de Sponsor', default='entreprise'),
        'categorie': fields.selection(selection=[('bronze','Bronze'),('silver','Silver'),('gold','Gold'),('platinium','Platinium')], string='Categorie', default='bronze'),
        'budget': fields.float('Budget (en DHs)', required=True),
        'address': fields.char('Address'),
        'id_manifestation': fields.many2one('gms.ensah.manifestation', 'Manifestation', ondelete='no action'),
    }

gms_ensah_sponsor()