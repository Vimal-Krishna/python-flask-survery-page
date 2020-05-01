from flask import Flask, render_template, redirect, url_for
from wtforms import (Form, StringField, IntegerField, SelectField, 
    RadioField, BooleanField, TextAreaField, FormField)

app = Flask(__name__)

class NormalFields(Form):
    name = StringField(label='Name')
    email = StringField(label='Email')
    age = IntegerField(label='Age (optional)')
    current_role_label = "Which options best describes your current role?"
    current_role_choices = [
        ('default', 'Select Current Role'),
        ('student', 'Student'),
        ('full_time_job', 'Full Time Job'),
        ('full_time_learner','Full Time Learner'),
        ('prefer_not_to_say','Prefer Not To Say'),
        ('other','Other')
    ]
    current_role_dropdown = SelectField(label=current_role_label,  
        choices=current_role_choices, default='default')

    recommend_label = "Would you recommend freeCodeCamp to a friend?"
    recommend_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('maybe', 'Maybe')
    ]
    recommend_radiobutton = RadioField(label=recommend_label,
        choices=recommend_choices)

    favorite_feature_label = "What is your favorite feature of freeCodeCamp?"
    favorite_feature_choices = [
        ('default', 'Select an option'),
        ('challenges', 'Challenges'),
        ('projects', 'Projects'),
        ('community', 'Community'),
        ('open_source', 'Open Source')
    ]
    favorite_feature_dropdown = SelectField(label=favorite_feature_label,
        choices=favorite_feature_choices)

class Checkboxes(Form):
    front_end_projects_checkbox = BooleanField("Front-end Projects")
    back_end_projects_checkbox = BooleanField("Back-end Projects")
    data_visualization_checkbox = BooleanField("Data Visualization")
    challenges_checkbox = BooleanField("Challenges")
    opensource_community_checkbox = BooleanField("Open Source Community")
    gitter_help_rooms_checkbox = BooleanField("Gitter Help Rooms")
    videos_checkbox = BooleanField("Videos")
    city_meetups_checkbox = BooleanField("City Meetups")
    wiki_checkbox = BooleanField("Wiki")
    forum_checkbox = BooleanField("Forum")
    additional_courses_checkbox = BooleanField("Additional Courses")

class SurveyForm(Form):
    normal_fields = FormField(NormalFields)
    checkboxes = FormField(Checkboxes)
    suggestions_textarea = TextAreaField("Any comments or suggestions?")
    
def home():
    return "hello from flask"

@app.route("/")
@app.route("/survey")
def survey():
    form = SurveyForm()
    return render_template('base.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='80')