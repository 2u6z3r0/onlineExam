$(document).ready(function(){
    exam_id = $("#data-js").attr("data-js-vars");
            $.get("/api/",{"id":exam_id},function(data,status){
                var i;
            //    alert(data);
                data2 = [];
               for(i=0;i<data.length;i++)
               {
                   if(data[i].exam == exam_id)
                   {
                       console.log(data[i].exam+' '+exam_id);
                       data2.push(data[i]);
                   }
               }
                i=0;
                //alert(data);
                data = data2;
                //console.log(data.length);
                if (data.length == 0 ) {
                    $("#no-questions").show();
                    return;
                }
                $("#question-display").show();
                //alert(questions);
                $(".question-place").html(data[i].question_text);
                $(".option1-place").html(data[i].option1);
                $(".option2-place").html(data[i].option2);
                $(".option3-place").html(data[i].option3);
                $(".option4-place").html(data[i].option4);
                $("#radio100").val(data[i].option1);
                $("#radio101").val(data[i].option2);
                $("#radio102").val(data[i].option3);
                $("#radio103").val(data[i].option4);
                $(".after").hide();
                test(data,0);
            });
    });

    function test(data,count)
    {
        j = 1;
        $(".select-option").click(function(){
            var optionvalue = $('input[name=group100]:checked').val(); 
            // $("option-answer").val($(this).find(".option").text());
            // alert(selValue)
            $(".before").hide();
            $(".after").show();
        });
        
        $("#after").click(function(){
            // $('input[name=group100]').attr('checked', false);
            // alert($('input[name=group100]:checked').val())
            // alert(data[j-1].correct_option)
            if($('input[name=group100]:checked').val() == data[j-1].correct_option)
            {
                count++;
                console.log(count)
            }
            if(j >= data.length)
            {
                $(".after").hide();
                $(".before").show();
                $("#question-display").hide();
                show_result(count,data.length);
                return;
            }
            $(".question-place").html(data[j].question_text);
            $(".option1-place").html(data[j].option1);
            $(".option2-place").html(data[j].option2);
            $(".option3-place").html(data[j].option3);
            $(".option4-place").html(data[j].option4);
            $(".after").hide();
            $(".before").show();
            j++;
        });
    }

    function show_result(count,total)
    {
        $("#count").text(count);
        $("#total").text(total);
        $("#score").slideDown();
    }

    $("#exit-btn").click(function(){
        alert('closing the things')
    });