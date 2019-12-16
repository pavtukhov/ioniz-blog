{% load static %}
{% block form %}

<form action='.' method='POST' class="contact-form">{% csrf_token %}{{ form.as_p }}
	<div class="row">
		<div class="col-lg-6">
			<input type="text" placeholder="Name">
		</div>
		<div class="col-lg-6">
			<input type="text" placeholder="E-mail">
		</div>
		<div class="col-lg-12">
			<input type="text" placeholder="Website (optional)">
			<textarea placeholder="Comment"></textarea>
		<button class="site-btn">comment submit<img src="{% static 'img/arrow-right.png' %}" alt=""></button>
		</div>
	</div>
</form>
{% endblock %}
  
