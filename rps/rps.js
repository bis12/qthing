Games = new Mongo.Collection("games");

if (Meteor.isClient) {
  Template.body.created = function() {
      this.games = Games.find({}, {sort: {round: -1 }, limit: 5});
  }

  Template.body.helpers({
    games: function () {
      return Template.instance().games;
    }
  });

  Template.body.events({
    "click .new-play": function (event) {
      event.preventDefault();
      var current_round = Template.instance().games.fetch()[0].round
      Games.insert(
          {
            p1: event.target.name,
            round: current_round + 1
          }
      );
    }

  });
}

if (Meteor.isServer) {
    Games._ensureIndex({round: 1}, {unique: 1});
}
