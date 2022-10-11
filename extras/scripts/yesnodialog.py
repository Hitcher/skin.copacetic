#include <kodi/gui/dialogs/YesNo.h>

bool ret = kodi::gui::dialogs::YesNo::ShowAndGetInput(
   "Yes / No test call",   // The Header
   "You has opened Yes / No dialog for test",
   "",
   "Is this OK for you?",
   "Not really",           // No label, is optional and if empty "No"
   "Ohhh yes");            // Yes label, also optional and if empty "Yes"
fprintf(stderr, "You has called Yes/No, returned '%s'\n",
         ret ? "yes" : "no");
