import type { NextConfig } from "next";

const nextConfig = {
  logging: {
    fetches: {
      fullUrl: false,
      hmrRefreshes: false,
    },
    incomingRequests: false,
  },
} as any;


export default nextConfig;
