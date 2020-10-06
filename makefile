all:
	gcc -shared -o pynpoint/libmcp.so -fPIC src/mcp_com.c