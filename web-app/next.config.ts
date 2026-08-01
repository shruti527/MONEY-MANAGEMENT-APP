import type { NextConfig } from "next";

const nextConfig = {
  turbopack: {
    root: process.cwd(),
  },
  logging: {
    fetches: {
      fullUrl: false,
      hmrRefreshes: false,
    },
    incomingRequests: false,
  },
} as any;


export default nextConfig;
