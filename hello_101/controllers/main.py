# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Hello101Controller(http.Controller):
    
    @http.route('/hello_101/hello', type='json', auth='user')
    def get_hello_message(self, **kwargs):
        """Return hello message for the current user"""
        user = request.env.user
        company = user.company_id.name or 'Bringout'
        
        return {
            'message': f'{company} says hello to {user.name}!',
            'user_name': user.name,
            'company_name': company,
            'timestamp': str(http.datetime.now()),
        }
    
    @http.route('/hello_101/dashboard', type='http', auth='user', website=True)
    def dashboard(self, **kwargs):
        """Render dashboard page"""
        return request.render('hello_101.dashboard_template')
