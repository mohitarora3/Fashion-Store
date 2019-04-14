
   $(function(){
    let discountArray=new Set();
    let priceArray=new Set();
   var data={'Type':[],
    'Brand':
    [],
    'Price':[],
    'Discount':[],
    'Gender':[],
  };

  $("input.radiobutton-1").on("click",function(){
    var gender=$(this).val();
    data['Gender']=gender;
    console.log(gender);
    $.ajax({
      data:JSON.stringify(gender),
      type:"POST",
      contentType: 'application/json;charset=UTF-8',
      url:'/items/gender',
      success:function(filter_result){

         $('.filter').html(filter_result);
        }
    })
  });

  $("input.checkbox-1").on("click",function(){
      var $x=$(this).val();
      console.log($x);
      var newItem={'Brand':$x};
      console.log(newItem);

      var index=data['Brand'].findIndex(x=>x['Brand']==$x);
      console.log(index);
      console.log('yippy')
      // var ans=$'input[data-panelId="checkbox-1"]';
      // console.log(ans);
      // var checkbox_type=$('this').attr("data-panelId");
      // alert(checkbox_type);
     // data['Brand']={"Brand":$x};
     var isChecked=$(this).is(':checked');
     if(isChecked && index==-1)
        data['Brand'].push(newItem); //inserting  of brands
      else
        data['Brand'].splice(index,1); //to remove brand that is unchecked (right now by user)
      //splice(index,number_of_elements_to_delete) //index - start point of deletion


    });

   $("input.checkbox-4").on("click",function(){
      var $x=$(this).val();
      console.log($x);
      var newType={'Type':$x};
      console.log(newType);

      var index=data['Type'].findIndex(x=>x['Type']==$x);
      console.log(index);
      console.log('yippy')
      // var ans=$'input[data-panelId="checkbox-1"]';
      // console.log(ans);
      // var checkbox_type=$('this').attr("data-panelId");
      // alert(checkbox_type);
     // data['Brand']={"Brand":$x};
     var isChecked=$(this).is(':checked');
     if(isChecked && index==-1)
        data['Type'].push(newType); //inserting  of brands
      else
        data['Type'].splice(index,1); //to remove brand that is unchecked (right now by user)
      //splice(index,number_of_elements_to_delete) //index - start point of deletion


    });


  $("input.checkbox-2").on("click",function(){
      var newPrice,isChecked,index,$x=$(this).val();
      var newPrice=parseInt($x);
      console.log(newPrice);
      // index=data['Discount'].findIndex(x=>x['Discount']==$x);
      isChecked=$(this).is(':checked');
      if(isChecked)
      {
                    priceArray.add(newPrice);
                   data['Price']=Array.from(priceArray);
                  // minDiscount=Math.min.apply(0,data['Discount']);

      }
      else
      {
          priceArray.delete(newPrice);
          data['Price']=Array.from(priceArray);
      }

        console.log(data['Price']);

  });

  $("input.checkbox-3").on("click",function(){
      var newDiscount,isChecked,index,$x=$(this).val();
      var newDiscount=parseInt($x);
      console.log(newDiscount);
      // index=data['Discount'].findIndex(x=>x['Discount']==$x);
      isChecked=$(this).is(':checked');
      if(isChecked)
      {
                    discountArray.add(newDiscount);
                   data['Discount']=Array.from(discountArray);
                  // minDiscount=Math.min.apply(0,data['Discount']);

      }
      else
      {
          discountArray.delete(newDiscount);
          data['Discount']=Array.from(discountArray);
 }

        console.log(data['Discount']);

  });



  $(':checkbox').on('click',function(){

    console.log('yes',data);

    $.ajax({
      data:JSON.stringify(data),
      type:"POST",
      contentType: 'application/json;charset=UTF-8',
      url:'/items/filter',
      success:function(items){
        console.log(items);
         $('.eighty').html(items);
        }
    })
  });

  });
