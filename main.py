i = raw_input('Cell created. Kill? (y/n)\n');

while (i):
  if ('y' == i):
    print("Cell killed\n");
    break;
  i = raw_input("Cell cloned. Kill? (y/n)\n");

