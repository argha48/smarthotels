#!/usr/bin/env python
#############################################################
#	Copyright (C) 2019  Argha Mondal
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
#############################################################
from flask import render_template
from flask import request
from flaskexample import app
from src.demo import *


@app.route('/')
@app.route('/index')
def index():
    # alldata = pd.read_json('./src/ahotel.json', orient='columns',encoding='utf-8')
    alldata = pd.read_json('./src/minidemo.json',orient='columns',encoding='utf-8')
    def get_text(rev):
        return rev[0] if str(rev)!='nan' else ''
    dfc = alldata[['HotelName']].copy()
    data = dfc['HotelName'].unique()
    return render_template("index.html", data=data)

@app.route('/slides')
def slides():
    return render_template("slides.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/topics', methods=['POST'])
def my_form_post():
    from flask import session
    hotel_name = str(request.form['hotel_name'])
    hotel_star = str(request.form['hotel_star'])
    session['hotel_name'] = request.form.get('hotel_name')
    session['hotel_star'] = request.form.get('hotel_star')
    return render_template("topics.html",data=score_compare(hotel_name, hotel_star))

@app.route('/topics_details', methods=['GET','POST'])
def topics_details():
    from flask import session
    hotel_name = session.get('hotel_name',None)#'Adelphi Hotel'#
    hotel_star = session.get('hotel_star',None)#'5'#
    atopic = str(request.form['atopic'])#'Topic_0'#
    ntop={
            'Hotel Staff':0,
            'Accessibility':1,
            'Food':2,
            'Overall Experience':3,
            'Noise':4,
            'Value for Money':5,
            'Room Amenities':6,
            'Location in the city':7,
            'Overall Experience':8,
            'Cleanliness':9,
            'Early Check-in/Late Check-out':10,
            'Health and Wellness Amenities':11,
            'Booking Experience':12,
            'Sleep Quality':13,
            'Parking Facility':14}

    ptopic = 'Topic_'+str(ntop[atopic])
    from bokeh.embed import components
    plot = compare_plot(hotel_name,hotel_star,ptopic)
    script, div = components(plot)
    return render_template("topics_details.html", script=script, div=div, data = [hotel_name,str(int(hotel_star)+1),atopic])
