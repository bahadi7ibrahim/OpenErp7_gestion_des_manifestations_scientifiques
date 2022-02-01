from osv import osv,fields
# import openerp


class gms_ensah_manifestation(osv.osv):
    def _Sponsoring(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'sponsor'})
        return True

    def _Preparing(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'preparation'})
        return True        

    def _Organisation(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'organisation'})
        return True    

    def _Starting(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'commence'})
        return True   

    def _Done(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'done'})
        return True    

    def _Postponed(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'reporte'})
        return True  

    def _Canceled(self,cr,uid,ids,context=None):
        self.write(cr,uid,ids,{'state':'annule'})
        return True  
        


    _name= 'gms.ensah.manifestation'
    _columns={
        'theme': fields.selection(selection=[('1','Informatique'),('2','Physique & Chimie'),('3','Energetique & energies renouvlables'),('4','Civil'),('5','Environnement')], string='Theme', default='1'),
        'name': fields.char('Titre',required=True),
        'date': fields.date('Date de manifestation',required=True),
        'duree':fields.integer('duree (en heures)') ,
        'budget':fields.float('budget (en DHs)',required=True)  ,
        'n_participant':fields.integer('nombre de participants')  ,
        'state':fields.selection([
            ('sponsor','Recherche de sponsor'),
            ('preparation','En cours de preparation'),
            ('organisation',"En cours d'organisation"),
            ('commence','Commencee'),
            ('done','Terminee'),
            ('annule','Annulee'),
            ('reporte','Reportee')]
            ,'state'),


        'id_participant':fields.one2many('gms.ensah.participant', 'id_manifestation', ondelete='no action',string='Participants'),
        'id_sponsor':fields.one2many('gms.ensah.sponsor', 'id_manifestation', ondelete='no action', string='Sponsors'),
        'id_intervenant':fields.one2many('gms.ensah.intervenant', 'id_manifestation', ondelete='no action', string='Intervenants'),
        'id_organisateur':fields.one2many('gms.ensah.organisateur', 'id_manifest', ondelete='no action', string='Organisateurs'),
        'id_local':fields.one2many('gms.ensah.local', 'id_man', ondelete='no action', string='Locals'),
        'id_responsable':fields.one2many('gms.ensah.responsable', 'id_manifes', ondelete='no action', string='Responsables'),
    }
    _defaults={
        'state':lambda *arg:"sponsor",
        'n_participant':lambda *arg:0,
    }
gms_ensah_manifestation()