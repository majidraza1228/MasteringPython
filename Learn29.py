def whoami():
      def local_groot():
        i = "I am local groot"
    ## the i variable above will not be recognized by the whoami() funciton.
      i = "I am groot"
      print(i)
      local_groot()
      print(i)  
  # printing i here will not print the i defined in local_groot() since it's scope does not reach whoami()
whoami()

