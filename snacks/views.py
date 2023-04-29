from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snacks"] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Peanut-Butter-Jelly-Sandwich.jpg/640px-Peanut-Butter-Jelly-Sandwich.jpg",
                "title": "PB&J",
                "description": "The classic Peanut Butter and Jelly Sandwich. Scrumptious for all ages.",
                "reference_url": "https://en.wikipedia.org/wiki/Peanut_butter_and_jelly_sandwich"
            }, {
                "image_url": "https://lilluna.com/wp-content/uploads/2014/02/fruit-smoothie-resize-14.jpg",
                "title": "Smoothie",
                "description": "A fruit smoothie is a great way to kick off any day!",
                "reference_url": "https://lilluna.com/fruit-smoothie/"
            }, {
                "image_url": "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2018/3/30/0/LS-Library_Garlic-Herb-Mixed-Nut-Snack-Mix_s4x3.jpg.rend.hgtvcom.616.462.suffix/1522443818679.jpeg",
                "title": "Mixed Nuts",
                "description": "Mixed Nuts can be great for chowing down.",
                "reference_url": "https://www.foodnetwork.com/recipes/food-network-kitchen/garlic-herb-mixed-nut-snack-mix-5481684"
            },
        ]

        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'