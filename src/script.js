$(function() { // On DOM content ready...
  var urls = {};

  $('div a').each(function() {
    var index = $(this).attr("class");
    console.log(index);
    if (typeof urls[index] === 'undefined'){
      urls[index] = [];
    }
    urls[index].push(this.href); // Store the URLs from the links...
  });

  console.log(urls);

  $('h3').click(function() {
    var index = $(this).attr("id");
    index = "links_" +  index;
    for (var i in urls[index]){
      window.open(urls[index][i]);
    }
  })
});