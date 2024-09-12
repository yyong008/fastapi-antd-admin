import request from "@/utils/request";

type TMonitorLoginLog = {
  page: number;
  pageSize: number;
}

export const getMonitorLoginLog = async (searchParams : TMonitorLoginLog) => {
  try {
    const res = await request.get("/api/admin/system/monitor/login-log", {
      params: { page: searchParams.page, size: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};
