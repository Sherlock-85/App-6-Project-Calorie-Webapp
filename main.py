from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):
        def get(self):
            caloriesform = CaloriesForm()
            return render_template('calories_form_page.html', caloriesform=caloriesform)

        def post(self):
            caloriesform = CaloriesForm()
            weight = caloriesform.weight.data
            height = caloriesform.height.data
            age = caloriesform.age.data
            city = caloriesform.city.data
            country = caloriesform.country.data

            temperature = Temperature(country=country, city=city).get()

            required_calories = Calorie(weight=weight, height=height, age=age, temperature=temperature.get())
            return render_template('calories_form_page.html', result=True, caloriesform=caloriesform,
                                   calories=required_calories.calculate())


class CaloriesForm(Form):
    weight = StringField("Weight: ", default= 175)
    height = StringField("Height: ", default=70)
    age = StringField("Age: ", default=35)
    city = StringField("City: ", default='New-York')
    country = StringField("Country: ", default='USA')

    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form',
                 view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)
