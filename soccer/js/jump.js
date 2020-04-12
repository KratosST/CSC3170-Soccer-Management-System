// Jump inside page
$(".toc>li>a").click(function () {
    $(this).addClass("hover");
    $(this).next().slideToggle();
    $(this).parent().siblings().children("a").removeClass("hover").next().slideUp();

})

// Jump to another page
$(function(){
    name = $("#name").text();
    age = $("#age").text();

   $("#btn").on("click",function(){
      jump1();
   });
});

function jump1(){
   url = "b.html?name="+name+"&age="+age;//此处拼接内容
   window.location.href = url;
}

$(function () {
    getData1();
});

function getData1() {
    var name = $.query.get("name");
    var age = $.query.get("age");

    $("#name").text(name);
    $("#age").text(age);
}