function PnlTable({ data }) {
  return (
    <div className="table-wrapper">
      <table className="pnl-table">
        <thead>
          <tr>
            <th>Strategy</th>
            <th>P&L</th>
          </tr>
        </thead>

        <tbody>
          {data.map((row) => (
            <tr key={row.strategy}>
              <td>{row.strategy}</td>
              <td>{row.pnl}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default PnlTable;