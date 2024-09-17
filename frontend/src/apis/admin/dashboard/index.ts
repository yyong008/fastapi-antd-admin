import request from "@/utils/request";

export const getDashboardData = async () => {
  try {
    const res = await request.get("/api/admin/dashboard/");
    return res;
  } catch (error) {
    console.error(error);
  }
};
