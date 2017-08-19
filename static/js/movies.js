$(function() {
  //Model
  var movie = Backbone.Model.extend({
  });

  //collection
  var movies = Backbone.Collection.extend({
    model: movie,
    url: "/todo/"
  });
  var list = new movies;

  //router
  var AppRouter = Backbone.Router.extend({
    routes: {
        ":router_name" : "renderPlayingPage",
    },

    renderPlayingPage: function(router_name) {
        var playingPage = new moviesView;
        playingPage.render(router_name);
    }
  });

  //app view
  var appView = Backbone.View.extend({
    initialize: function() {
      this.listenTo(list, 'reset', this.render);
      list.fetch({reset: true});
    },

    render: function() {
      list.each(function(movie) {
        var template = _.template($("#movies_template").html());
        var constPath = "./static/source/";
        $("#list").append(template({
          name: movie.get('name'),
          actress: movie.get('actress'),
          getModal: "#"+movie.get('name')+"Modal",
          theModal: movie.get('name')+"Modal",

          router_name: constPath +
                       movie.get('time') + "video/" +
                       "#"+ movie.get('name') + "." + movie.get('videoFormat'),
          oriPhoto: constPath + movie.get('time') + "image/" +
                       movie.get('name') + ".jpg",
          resizePhoto: constPath + movie.get('time') + "image/" +
                       "r_" + movie.get('name') + ".jpg",
          buttonType: constPath +
                       movie.get('buttonType')+"_player.png",
        }));
      });
    }
  });

  //movies View
  var moviesView = Backbone.View.extend({
    initialize: function() {
    },
    render: function(name) {
      $("#list").hide();
      var template = _.template($("#playing_template").html());
      $("body").append(template({
        video_path : name,

      }));
    },
  });

  //start appliction
  app = new appView;

  //star router
  var app_router = new AppRouter;
  Backbone.history.start();
});
