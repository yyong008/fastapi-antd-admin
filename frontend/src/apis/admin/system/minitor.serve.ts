import request from "@/utils/request";

export const getMonitorServe = async () => {
  try {
    const res = await request.get("/api/admin/system/monitor/serve");
    return res;
  } catch (error) {
    console.error(error);
  }
};
