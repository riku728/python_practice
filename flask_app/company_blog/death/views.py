from flask import render_template, url_for, redirect, session, flash, request, abort
from flask_login import login_user, logout_user, login_required, current_user
# from company_blog import db
# from company_blog.models import User, BlogPost, BlogCategory
# from company_blog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
# from company_blog.main.forms import BlogSearchForm
from datetime import datetime, timedelta
from flask import Blueprint

death = Blueprint('death', __name__)

@death.route('/death_counter', methods=['GET', 'POST'])
def death_counter():
    if request.method == 'POST':
        birthdate_str = request.form['birthdate']
        lifespan = int(request.form['lifespan'])

        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
        deathdate = birthdate.replace(year=birthdate.year + lifespan)
        now = datetime.now()
        delta = deathdate - now

        # 各単位で残り時間を計算
        remaining_years = delta.days // 365
        remaining_weeks = delta.days // 7
        remaining_days = delta.days
        remaining_seconds = int(delta.total_seconds())
        remaining_hours = remaining_seconds // 3600
        remaining_minutes = remaining_seconds // 60

        # 残りの土日を数える
        weekends = 0
        current = now
        while current < deathdate:
            if current.weekday() in [5, 6]:  # 土・日
                weekends += 1
            current += timedelta(days=1)

        return render_template(
            'death/death_counter_result.html',
            years=remaining_years,
            weeks=remaining_weeks,
            days=remaining_days,
            hours=remaining_hours,
            minutes=remaining_minutes,
            seconds=remaining_seconds,
            weekends=weekends
        )
    return render_template('death/death_counter_form.html')