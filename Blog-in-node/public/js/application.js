$(function(){

	var ApplicationRouter = Backbone.Router.extend({

		//map url routes to contained methods
		routes: {
			"": "createblog",
			"create":"createblog",
 
			"read": "readblog",
			"logout": "logout"
		},

		deselectPills: function(){
			//deselect all navigation pills
			$('ul.pills li').removeClass('active');
		},

		selectPill: function(pill){
			//deselect all navigation pills
			this.deselectPills();
			//select passed navigation pill by selector
			$(pill).addClass('active');
		},

		hidePages: function(){
			//hide all pages with 'pages' class
			$('div.pages').hide();
		},

		showPage: function(page){
			//hide all pages
			this.hidePages();
			//show passed page by selector
			$(page).show();
		},

		createblog: function() {
			this.showPage('div#create-page');
			this.selectPill('li.home-pill');
		},

		read: function() {
			this.showPage('div#read-page');
			this.selectPill('li.about-pill');
		},

		logout: function() {
                         window.location.assign("/logout");
			this.showPage('div#logout-page');
			this.selectPill('li.contact-pill');
		}

	});

	var ApplicationView = Backbone.View.extend({

		//bind view to body element (all views should be bound to DOM elements)
		el: $('body'),

		//observe navigation click events and map to contained methods
		events: {
			'click ul.pills li.home-pill a': 'displayHome',
			'click ul.pills li.about-pill a': 'displayAbout',
			'click ul.pills li.contact-pill a': 'displayContact'
		},

		//called on instantiation
		initialize: function(){
			//set dependency on ApplicationRouter
			this.router = new ApplicationRouter();

			//call to begin monitoring uri and route changes
			Backbone.history.start();
		},

		displayHome: function(){
			//update url and pass true to execute route method
			this.router.navigate("create", true);
		},

		displayAbout: function(){
			//update url and pass true to execute route method
			this.router.navigate("read", true);
		},

		displayContact: function(){
			//update url and pass true to execute route method
			this.router.navigate("logout", true);
		}

	});

	//load application
	new ApplicationView();

});

