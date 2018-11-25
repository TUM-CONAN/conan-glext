#ifdef _WIN32

// target XP
#ifndef WINVER
	#define WINVER 0x0501
#endif

#ifndef _WIN32_WINNT
	#define _WIN32_WINNT WINVER
#endif

#ifndef WIN32_LEAN_AND_MEAN
	#define WIN32_LEAN_AND_MEAN
	#define UBITRACK_UNDEF_WIN32_LEAN_AND_MEAN
#endif

#ifndef NOMINMAX
	#define NOMINMAX
	#define UBITRACK_UNDEF_NOMINMNAX
#endif

#include <Windows.h>

#ifdef UBITRACK_UNDEF_NOMINMNAX
	#undef NOMINMAX
#endif

#ifdef UBITRACK_UNDEF_WIN32_LEAN_AND_MEAN
	#undef WIN32_LEAN_AND_MEAN
#endif

#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glext.h>
#elif __APPLE__
#include <OpenGL/gl.h>
#include <OpenGL/glu.h>
#else
#include <GL/gl.h>
#include <GL/glext.h>
#include <GL/glu.h>
#include <GL/glx.h>
#endif


int main()
{
	return 0;
}
