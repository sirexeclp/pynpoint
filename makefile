all:
	gcc -shared -o libmcp.so -fPIC c_src/mcp_com.c