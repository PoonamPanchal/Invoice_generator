function insert_Row()
{
    
var rows=document.getElementById('tbody').rows.length;	
var x= document.getElementById('tbody').insertRow(-1);
var a = x.insertCell(0);
var b = x.insertCell(1);
var c = x.insertCell(2);
var d = x.insertCell(3);
var e = x.insertCell(4);
var f = x.insertCell(5);


a.innerHTML="<input type='text' class='input' id='name"+rows+"' name='name' required>";
b.innerHTML="<input type='text' class='input'  id='price"+rows+"' name='price' oninput = 'amount_calc(this.id)' required>";
c.innerHTML="<input type='text' class='input' id='quantity"+rows+"' name='quantity' oninput = 'amount_calc(this.id)' required>";
d.innerHTML="<input type='text' class='input' id='amount"+rows+"' name='amount' value=0 readonly required>";
e.innerHTML="<input type='text' class='input' id='tax"+rows+"' name='tax' value=0 oninput = 'amount_calc(this.id)' required>";
f.innerHTML="<input type='text' class='input' id='total"+rows+"' name='total' value=0 readonly required>";
}

function amount_calc(id)
{
suff=id.slice(-1);
var quantity=document.getElementById('quantity'+suff).value;
var price=document.getElementById('price'+suff).value;
var amount=price*quantity;
document.getElementById('amount'+suff).value=amount;
var gst=document.getElementById('tax'+suff).value;
var total = amount*gst/100+amount;
var total_amount=document.getElementById('total'+suff);
total_amount.value=total;
// var grand_total =document.getElementById('grand_total').value;
var total_rows =document.getElementById('tbody').rows.length;	
var grand_total_field=document.getElementById('grand_total');
var grand_total=0;
for(i=0;i<total_rows;i++)
{
    var a= parseFloat(document.getElementById('total'+i).value);
    grand_total=grand_total+a;

}

grand_total_field.value=grand_total;



}

