<?php
	$connection = mysqli_connect("localhost","root","");
	$db = mysqli_select_db($connection,"sms");

	$rollNo = $_POST['roll_no'];
	$name=$_POST['name'];
	$father_name=$_POST['father_name'];
	$class=$_POST['class'];
	$mobile=$_POST['mobile'];
	$email=$_POST['email']; 
	$password=$_POST['password'];
	$remark=$_POST['remark'];

	$query = "insert into students (roll_no,name,father_name,class,mobile,email,password,remark) values('$rollNo','$name','$father_name', '$class','$mobile','$email','$password','$remark')";
	$query_run = mysqli_query($connection,$query);
?>
<script type="text/javascript">
	alert("Student added successfully.");
	window.location.href = "admin_dashboard.php";
</script>