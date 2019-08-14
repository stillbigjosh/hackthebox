<!DOCTYPE html>
<html lang="en" >

<head>
  <meta charset="UTF-8">
  <title>Support Login Page</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  
  <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css'>
<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'>

      <link rel="stylesheet" href="css/style.css">

  
</head>

<body>

  <div id="particles-js"></div>
<body class="login">
	<div class="container">
		<div class="login-container-wrapper clearfix">
			<div class="logo">
				<i class="fa fa-sign-in"></i>
			</div>
			<div class="welcome"><strong>Welcome,</strong> please login</div>

			<form class="form-horizontal login-form" method="POST" action="<?php echo $_SERVER['PHP_SELF']; ?>">
				<div class="form-group relative">
					<input id="login_username" name="login_username" class="form-control input-lg" type="email" placeholder="Username" required>
					<i class="fa fa-user"></i>
				</div>
				<div class="form-group relative password">
					<input id="login_password" name="login_password" class="form-control input-lg" type="password" placeholder="Password" required>
					<i class="fa fa-lock"></i>
				</div>
			  <div class="form-group">
			    <button name="login" type="submit" class="btn btn-success btn-lg btn-block">Login</button>
			  </div>
        <div class="checkbox pull-left">
			    <label><input type="checkbox" name="remember"> Remember</label>
			  </div>
			  <div class="checkbox pull-right">
			    <label> <a class="forget" href="/login.php?guest=true" title="forget">Login as guest</a> </label>
			  </div>
			</form>
		</div>
    
    <h4 class="text-center">
      <a target="_blank" href="">
	24 x 7 Support
      </a>
    </h4>
	</div>

  </body>
  <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js'></script>
<script src='https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js'></script>

  

    <script  src="js/index.js"></script>




</body>
<?php
session_start();
if( isset($_REQUEST['login']) && !empty($_REQUEST['login_username']) && !empty($_REQUEST['login_password'])) {
	if( $_REQUEST['login_username'] === 'admin@support.htb' && hash( 'sha256', $_REQUEST['login_password']) === '91c077fb5bcdd1eacf7268c945bc1d1ce2faf9634cba615337adbf0af4db9040') {
		$_SESSION['admin'] = "valid";
		header('Location: issues.php'); 
	}
	else
		header('Location: errorpage.php');
}
else if( isset($_GET['guest']) ) {
	if( $_GET['guest'] === 'true' ) {
		$_SESSION['guest'] = "valid";
		header('Location: issues.php');
	}
}


?>
</html>

