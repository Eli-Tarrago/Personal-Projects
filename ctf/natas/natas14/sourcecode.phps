
<?
if(array_key_exists("username", $_REQUEST)) {
   $link = mysql_connect('localhost', 'natas14', '<censored>');
   mysql_select_db('natas14', $link);

   $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"
       and password=\"".$_REQUEST["password"]."\"";
   if(array_key_exists("debug", $_GET)) {
       echo "Executing query: $query<br>";
   }

   if(mysql_num_rows(mysql_query($query, $link)) > 0) {
           echo "Successful login! The password for natas15 is <censored><br>";
   } else {
           echo "Access denied!<br>";
   }
   mysql_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password"><br>
<input type="submit" value="Login" />
</form>
<? } ?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
</body>
</html>
