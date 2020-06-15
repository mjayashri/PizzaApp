document.addEventListener('DOMContentLoaded', () => {

  // set important variables
  //var size_dic = {};
  var prices_dic = {};

  var foods_selector = document.getElementById("foods_choice");
  var prices_selector = document.getElementById("prices_choice");


  // change selectors style to hidden
  //document.getElementById('foods_selector').style.display = 'none';
  document.getElementById('prices_selector').style.display = 'none';


      // set event on selecting a food item (adding to cart)
      foods_selector.onchange = () => {

    // get the selected food value
    let index1 = foods_selector.selectedIndex;
    var selected_food = (foods_selector.options[index1].value);
    // create new key for the selected food item's prices list
    prices_dic[`${selected_food}`] = []


    // get all prices for that food from the menu
    let foods_prices = document.getElementsByClassName(`${selected_food}`)
    for (let i = 0; i < foods_prices.length; i++) {
      prices_dic[`${selected_food}`].push(foods_prices[i].innerHTML);
      //prices_dic[`${selected_food}`].push(foods_prices[i].innerHTML);

    }
    // prepare the foods selection
    while (prices_selector.options.length) {
      prices_selector.remove(0);
    }
    // adding empty choice in the selector
    let empty_choice = new Option('Choose Item ...', '')
    prices_selector.options.add(empty_choice)

    var prices_list = prices_dic[`${selected_food}`]
    // put the food items in the selection element
    if (prices_list) {
      for (let i = 0; i < prices_list.length; i++) {
        var aprice = new Option(prices_list[i], i);
        prices_selector.options.add(aprice);
      }
    }
    document.getElementById('prices_selector').style.display = 'block';
  };


  document.querySelector("button[type='submit']").onclick = () => {
  }

  document.getElementById("place_order").onclick = () => {
    alert('are you sure you want to place this order ?');
    return true
  }

});





