$(document).ready(function () {
    $(".like-btn").on("click", function () {
        var id = $(this).attr("note_id");
        
        const btn = $(this);
        // btn.addClass("hidden");

        // alert(id);


        axios.post('/like', {
            note_id: id
          })
          .then(function (response) {
            if (response.data.msg==="like_set") {
                btn.removeClass();
                btn.addClass("like-btn text-white border border-red-700 bg-red-700 hover:bg-red-800 focus:outline-none font-medium rounded-full text-sm px-5 py-2.5 text-center mr-2 dark:bg-red-600 dark:hover:bg-red-700");
                var a = btn.parent().children(".likes_count").text();
                btn.text("Unlike");
                btn.parent().children(".likes_count").text(parseInt(a)+1);
            } 
            if (response.data.msg==="like_removed") {
                btn.removeClass();
                btn.addClass("like-btn text-gray-900 bg-white border border-gray-300 hover:bg-gray-100 font-medium rounded-full text-sm px-5 py-2.5 mr-2 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600");
                var a = btn.parent().children(".likes_count").text();
                btn.text("Like");
                btn.parent().children(".likes_count").text(parseInt(a)-1);
            } 
            // btn.parent().children(".likes_count").text("asdf")


            

            //  console.log(foo(id));
            
          })
          .catch(function (error) {
            console.log(error);
          });

        // var x = fetch("/get_likes_count/" + id)
        //     .then((response) => response.json())
        //     .then((responseJSON) => {
        //         btn.parent().children(".likes_count").text(responseJSON.count);
        //         // console.log("did it" + responseJSON.count)
        // });

    

    });

});


