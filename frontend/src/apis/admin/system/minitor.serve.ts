import request from "@/utils/request";

export const getMonitorServe = async () => {
  try {
    const res = await request.get("/api/admin/system/monitor/serve");
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getMonitorServeById = async (id: number) => {
  try {
    const res = await request.get(`/api/admin/system/monitor/serve/${id}`);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const createMonitorServe = async (data: any) => {
  try {
    const res = await request.post("/api/admin/system/monitor/serve", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const updateMonitorServe = async (id: number, data: any) => {
  try {
    const res = await request.put(`/api/admin/system/monitor/serve/${id}`, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteMonitorServe = async (ids: number[]) => {
  try {
    const res = await request.delete(`/api/admin/system/monitor/serve/`, {
      data: {
        ids
      }
    });
    return res;
  } catch (error) {
    console.error(error);
  }
}
