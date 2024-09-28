import request from "@/utils/request";

type TMonitorLoginLog = {
  page: number;
  pageSize: number;
};

export const getMonitorLoginLog = async (searchParams: TMonitorLoginLog) => {
  try {
    const res = await request.get("/api/admin/system/monitor/login-log", {
      params: { page: searchParams.page, size: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getMonitorLoginLogById = async (id: string) => {
  try {
    const res = await request.get("/api/admin/system/monitor/login-log/" + id);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const createMonitorLoginLog = async (data: any) => {
  try {
    const res = await request.post("/api/admin/system/monitor/login-log", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const updateMonitorLoginLog = async (id: string, data: any) => {
  try {
    const res = await request.put("/api/admin/system/monitor/login-log/" + id, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteMonitorLoginLog = async (ids: number[]) => {
  try {
    const res = await request.delete("/api/admin/system/monitor/login-log/", {
      data: {
        ids
      }
    });
    return res;
  } catch (error) {
    console.error(error);
  }
}
