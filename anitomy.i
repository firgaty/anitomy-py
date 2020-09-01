%module anitomy
%{
#include "anitomy/anitomy.h"

using string_t = std::wstring;

using namespace anitomy;
%}

%include "std_string.i"
%include "std_wstring.i"

%include "anitomy/options.h"
%include "anitomy/element.h"
%include "anitomy/anitomy.h"

using string_t = std::wstring;
