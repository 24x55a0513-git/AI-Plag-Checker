const file1=document.getElementById("file1");
const file2=document.getElementById("file2");

file1.addEventListener("change",function(){

const name=this.files[0]?.name || "No file selected";

document.getElementById("file1-name").innerHTML=
"✅ "+name;

});

file2.addEventListener("change",function(){

const name=this.files[0]?.name || "No file selected";

document.getElementById("file2-name").innerHTML=
"✅ "+name;

});