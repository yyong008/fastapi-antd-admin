export const getResponse = async (data: any) => {
  const token = localStorage.getItem("token");
  const response = await fetch("/api/admin/langchain/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Network response was not ok");
  }
  return response;
};
